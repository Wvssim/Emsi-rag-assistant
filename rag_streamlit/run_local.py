from rag import get_qa_chain


def main():
    qa = get_qa_chain()
    question = "Qu'est-ce que l'EMSI?"
    result = qa(question)
    print(result.get("result", ""))


if __name__ == "__main__":
    main()

