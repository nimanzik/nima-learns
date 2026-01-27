# git-grok

***A conversational Q&A agent built using Retrieval-Augmented Generation (RAG) to answer questions about code repositories.***

> [!NOTE]
> This project is for personal learning purposes only and is not intended for production use.

## Overview

The agent allows user to ask natural-language questions about the documentation of any public repository (at the moment, only GitHub is supported). It downloads Markdown and React Markdown files, intelligently chunks them using an LLM, and generates embeddings for each chunk. These embeddings are stored in a local vector database for semantic search.

At query time, the agent retrieves relevant documentation and uses it as context to generate accurate, repository-aware answers. This makes it easy to explore and understand large documentation sets quickly and without manual searching.

## How It Works

1. **Fetch**: Downloads and processes `.md` and `.mdx` files from a GitHub repository.
2. **Chunk**: Uses Google Gemini to split documents into logical sections.
3. **Embed & Store**: Generates embeddings using a pretrained [Sentence Transformers](https://www.sbert.net/index.html) (a.k.a SBERT) model and stores them locally via [Qdrant](https://qdrant.tech/) vector database.
4. **Search**: Performs semantic search to retrieve relevant context for Q&A.
5. **Answer**: Uses the retrieved context to generate a natural-language answer.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
