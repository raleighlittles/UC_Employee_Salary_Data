import parser
import retriever

if __name__ == "__main__":
    parser.parse(retriever.acquire_data(2018))
