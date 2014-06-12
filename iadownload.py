#! /usr/bin/env python

# Copyright 2014 VM Brasseur
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import internetarchive
import pprint
import argparse
import json

pp = pprint.PrettyPrinter(indent=2) #because I always need it

argsin = argparse.ArgumentParser(description="Download files from an Internet Archive collection.")
argsin.add_argument('--collection',
                dest="collection_id",
                help="Internet Archive collection identifier")
argsin.add_argument('--item',
                dest="item_id",
                help="Internet Archive item identifier")
argsin.add_argument('--outdir',
                dest="outdir",
                required=True,
                help="Directory where the files will be saved")
argsin.add_argument('--verbose',
                action="store_true",
                help="Have verbose output")

args = argsin.parse_args()

#-----
# Functions
#-----

def verboseout(string):
  # XXX Add different levels of verbosity
  if args.verbose:
    print string

def get_collection_items(collection_id):
  rv = []
  query = "(collection:" + collection_id + ")"
  searchresult = internetarchive.search.Search(query)
  for item in searchresult:
    rv.append(item['identifier'])
  return rv

def create_dir(basedir, identifier):
  newdir = basedir + "/" + identifier
  if os.path.exists(newdir):
    verboseout(newdir + " already exists. Not creating")
  else:
    verboseout(" Going to create" + newdir)
    os.makedirs(newdir) #XXX confirm this worked
    verboseout(newdir + " created")
  return newdir

def download_item_files(item_id):
  # XXX Add a repeatable --format flag for this rather than hard coding
  # XXX Alternatively: yaml config file
  f = ["Comic Book RAR", "EPUB", "Animated GIF", "Text PDF", "Image Container PDF"]
  i = internetarchive.Item(item_id)
  verboseout("Downloading files from " + i.identifier)
  if args.verbose:
    i.download(concurrent=True, verbose=True, ignore_existing=True, formats=f)
  else:
    i.download(concurrent=True, ignore_existing=True, formats=f)

#-----
# Set up some vars
#-----

outdir = args.outdir
collection_id = args.collection_id
item_id = args.item_id

#-----
# Sanity checks
#-----

# XXX Wait, I don't check whether --collection or --item are even defined? Really? Gotta fix that.

# either collection OR item; not both (yet)
if collection_id and item_id:
   print "Please use EITHER --collection OR --item, not both."
   sys.exit(0)

# Can open/write to outdir?
if os.path.isdir(outdir):
  verboseout(outdir + " exists and is a directory")
else:
  print outdir, " does not exist."
  sys.exit(0)

if os.access(outdir, os.W_OK):
  verboseout(outdir + " is writable")
else:
  print outdir, " is not writable."
  sys.exit(0)

#-----
# Start doing useful things
#-----
if collection_id:
  items = get_collection_items(collection_id)
  verboseout("Creating " + collection_id + " directory")
  collection_dir = create_dir(outdir, collection_id)
  os.chdir(collection_dir)
elif args.item_id:
  items = [item_id]
else:
  print "No collection_id and no item_id? That's not gonna work."

# XXX Verbose: print total num of items to download

for item in items:
  # XXX Verbose: print "num of total" countdown of item count
  download_item_files(item)
