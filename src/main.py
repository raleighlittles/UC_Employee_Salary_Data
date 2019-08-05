import src.parser
import src.retriever

if __name__ == "__main__":
    src.parser.parse(src.retriever.acquire_data(2018))
