#!/usr/bin/env python

import common
import chromatics
import os
import sys

from glob import glob

config_fn = sys.argv[1]
cell_line = config_fn.split('/')[0]
feature_name = config_fn.split('/')[1] # Added by R. Mendez 03/12/2018
config = common.parse_config(config_fn)
os.chdir(os.path.expanduser(config['working_dir']))

#segmentation_df = chromatics.read_bed(glob('../segmentation/*.bed.gz')[0], usecols = range(4), names = chromatics.generic_bed_columns)
segmentation_df = chromatics.read_bed(glob('./segmentation/' + cell_line + '*.bed.gz')[0], usecols = range(4), names = chromatics.generic_bed_columns ) # added by R Mendez 03/12/2018
#enhancer_states = {'E', 'WE', '13_EnhA1', '14_EnhA2', '16_EnhW1', '17_EnhW2'}
enhancer_states = {'E5', 'E6', 'E8'}} # added by R Mendez 03/12/2018
enhancers_df = segmentation_df.query('name in @enhancer_states and (end - start) > 4').copy()
enhancers_df.columns = chromatics.enhancer_bed_columns
chromatics.add_names(enhancers_df, cell_line = cell_line)

# optionally expand enhancer coordinates
enhancers_df['enhancer_start'] -= config['enhancer_extension_size'] if 'enhancer_extension_size' in config else 0
enhancers_df['enhancer_end'] += config['enhancer_extension_size'] if 'enhancer_extension_size' in config else 0

# save
assert enhancers_df.duplicated().sum() == 0
#chromatics.write_bed(enhancers_df, 'enhancers.bed')
chromatics.write_bed(enhancers_df, 'enhancers' + feature_name + '.bed') # added by R Mendez 03/12/2018
print(enhancers_df.eval('enhancer_end - enhancer_start').describe(), '\n')
