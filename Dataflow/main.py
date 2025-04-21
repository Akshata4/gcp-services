import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText

import argparse

def main():
    print('Pipeline starting')
    with beam.Pipeline(options=PipelineOptions(save_main_session=True)) as p:
        data = (p
                # | 'read data from file' >> ReadFromText())
                | 'create data' >> beam.Create(['akshata', 'madavi', 'is', 'good'])
                | 'print data' >> beam.Map(print)
        )
if __name__=='__main__':
    main()