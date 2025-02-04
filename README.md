# _AI Knowledge Engine_

A powerful AI-driven system integrating Retrieval-Augmented Generation (RAG), LangGraph, OpenAI embeddings, and Supabase for efficient document retrieval, processing, and conversational AI workflows.

## Features

- **Document Ingestion**: Load and split HTML documents into smaller chunks.
- **Vector Storage**: Store embeddings in Supabase for efficient retrieval.
- **RAG Pipeline**: Retrieve relevant context and generate answers using OpenAI.
- **LangGraph Integration (Coming Soon)**: Implement graph-based LLM workflows.
- **Chatbot Capabilities**: Extendable to real-time conversational AI.

## Tech Stack

- **Python** (Primary Language)
- **OpenAI API** (LLM & Embeddings)
- **Supabase** (Vector Database & Storage)
- **LangChain & LangGraph** (AI Workflow & Retrieval)
- **BeautifulSoup** (HTML Parsing)

## Setup Instructions

1. **Clone the Repository**
    ```sh
    git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
    cd YOUR_REPO_NAME
    ```

2. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**

    Create a `.env` file and add your credentials:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    SUPABASE_URL=your_supabase_url
    SUPABASE_KEY=your_supabase_key
    ```

4. **Run the Notebook**

    If using Jupyter Notebook, run:
    ```sh
    jupyter notebook
    ```
    Then, open the notebook and execute the cells step by step.


## Usage Workflow

1. **Load & Split Documents**: Extract text from HTML files.
2. **Generate & Store Embeddings**: Store document vectors in Supabase.
3. **Retrieve Relevant Chunks**: Match user queries with stored documents.
4. **Generate Answer**: Use OpenAI LLM to create responses.
5. **LangGraph Integration (Upcoming)**: Advanced AI workflow management.

## Roadmap

- ✅ Implement RAG-based document retrieval
- ✅ Store embeddings in Supabase
- ⏳ Integrate LangGraph for workflow automation
- ⏳ Develop chatbot functionalities
- ⏳ Optimize for real-time inference

## Contributing

Feel free to submit issues, suggestions, or pull requests!

## License

This project is licensed under the MIT License.

🚀 Built with AI & Passion 🚀
