import argparse

# local
import parser
import retriever

if __name__ == "__main__":
    
    argparse_parser = argparse.ArgumentParser()
    
    argparse_parser.add_argument("-y", "--year", type=int, help="The year you wish to download salary data for.")
    argparse_args = argparse_parser.parse_args()
    
    parser.parse(retriever.acquire_data(argparse_args.year))
