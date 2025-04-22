import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText

import argparse

class SplitRow(beam.DoFn):
    def process(self, element):
        name, age, country = element.split(",")
        return [{
            'name': name,
            'age': int(age),
            'country': country
        }]

def filter_age(record):
    return record['age'] > 40

def format_output(record):
    return f"{record['name']},{record['age']},{record['country']}"

def main():
    print('Pipeline starting')
    with beam.Pipeline(options=PipelineOptions(save_main_session=True)) as p:
        data = (p
                # | 'read data from file' >> ReadFromText())
                # | 'create data' >> beam.Create(['akshata', 'madavi', 'is', 'good'])
                # | 'print data' >> beam.Map(print)
                # | 'ReadInput' >> beam.io.ReadFromText('gs://apache-beam-samples/nasa_jpl_asteroid/full.csv')
                | 'ReadInput' >> beam.io.ReadFromText('input.txt')
                # | 'print data' >> beam.Map(print)
                | 'SplitRow' >> beam.ParDo(SplitRow())
                | 'FilterAge' >> beam.Filter(filter_age)
                | 'FormatOutput' >> beam.Map(format_output)
                | 'WriteOutput' >> beam.io.WriteToText('output.txt')
        )
if __name__=='__main__':
    main()