import os
import subprocess
import sys
import argparse

docker_name=""
kraken2_db=""

def run_kraken2(R1,R2,kraken2_db,outdir,prefix):
    cmd="docker run -v %s:%s "



