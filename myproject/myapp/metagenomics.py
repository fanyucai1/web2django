import os
import subprocess
import sys,json
import argparse

docker_name=""
kraken2_db=""

def fastp(R1,R2,outdir,prefix):
    out=outdir+"/"+prefix
    cmd="fastp -i %s -I %s -o %s.qc.R1.fq.gz " \
           "-O %s.qc.R2.fq.gz --dedup --thread 16 --low_complexity_filter " \
           "--length_required 36 " \
           "--html %s.qc.html --json %s.qc.json  > %s/log.txt 2>&1" % (R1,R2,out,out,out,out,out)
    subprocess.check_call(cmd, shell=True)
    outfile = open("%s.QC.tsv" % (out), "w")
    outfile.write(
        "SampleID\tTotal_reads\tTotal_bases\tQ20_rate\tQ30_rate\tgc_content\tTotal_reads(clean)\tTotal_bases\tQ20_rate\tQ30_rate\tgc_content\n")
    with open("%s.qc.json" % (out), "r") as load_f:
        load_dict = json.load(load_f)
        outfile.write("%s\t" % (prefix))
        outfile.write("%s\t%s\t%s\t%s\t%s\t"
                      % (load_dict['summary']['before_filtering']['total_reads'],
                         load_dict['summary']['before_filtering']['total_bases'],
                         load_dict['summary']['before_filtering']['q20_rate'],
                         load_dict['summary']['before_filtering']['q30_rate'],
                         load_dict['summary']['before_filtering']['gc_content']))
        outfile.write("%s\t%s\t%s\t%s\t%s\n"
                      % (load_dict['summary']['after_filtering']['total_reads'],
                         load_dict['summary']['after_filtering']['total_bases'],
                         load_dict['summary']['after_filtering']['q20_rate'],
                         load_dict['summary']['after_filtering']['q30_rate'],
                         load_dict['summary']['after_filtering']['gc_content']))

    outfile.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser("Pipline:quality cotrol(fastp)、taxonmy(kraken2) and assembly(megahit).")
    parser.add_argument("-r1","--read1",help="fastq R1 reads",required=True)
    parser.add_argument("-r2","--read2",help="fastq R2 reads",required=True)
    parser.add_argument("-d","--db",help="kraken2 database")
    parser.add_argument("-p","--prefix",help="prefix of output",required=True)
    parser.add_argument("-o","--outdir",help="output directory",required=True)
    args=parser.parse_args()
    fastp(args.r1,args.r2,args.outdir,args.prefix)