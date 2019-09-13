from .plage import convclass
import argparse
import sys

def main():

    parser = argparse.ArgumentParser(description="pla",formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--convert','-c', type=str,

                help='backend ML framework used to generate files')       

    
    args = parser.parse_args()
    sys.stdout.write(str(genfiles(args)))

def genfiles(args):
    if args.convert:
        print("converting....")
        par = convclass.conv(args.convert)
        return(par)


if __name__ == '__main__':

    main()