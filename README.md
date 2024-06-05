# Chatbot with Retrieval-Augmented Generation (RAG)

<p align="justify">This project contains a chatbot that takes a website URL as an input and allows users to chat with it. The chatbot's responses are based on its understanding of the website's content using the Retrieval-Augmented Generation (RAG) technique and OpenAI's API for language models (LLMs). RAG is a technique for augmenting LLM knowledge with additional data. LLMs can reason about wide-ranging topics, but their knowledge is limited to the public data up to a specific point in time that they were trained on. If you want to build AI applications that can reason about private data or data introduced after a model's cutoff date, you need to augment the knowledge of the model with the specific information it needs. The process of bringing the appropriate information and inserting it into the model prompt is known as Retrieval Augmented Generation (RAG).</p>

## Components
1. **main.py**: Main script to run the chatbot.
2. **processor.py**: Contains all the functions for the chatbot to work.
3. **requirements.txt**: Contains all packages to install.
4. **.env**: Contains the OpenAI API Key.

## Setup
1. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
2. Create a dotenv (.env) file to store OpenAI API key in the environment:
    ```
    OPENAI_API_KEY = {Your OpenAI API Key | Replace the entire brackets with the key}
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```

## Features
<p align="justify">This Python-based chatbot leverages LangChain's latest features to gather information from websites. It seamlessly interacts with OpenAI's API, utilizing the powerful GPT-4 language model (though it's flexible to work with others). The user interface is built with Streamlit, ensuring a user-friendly experience for anyone, regardless of technical background.</p>

## Contributing

<p align="justify">Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.</p>
  
**Note**: Always ensure to handle your API keys and sensitive data securely. Avoid committing them directly into public repositories.

## Connect with me:

<p align="justify">For any inquiries or issues, please open an issue on the GitHub repository or contact me through LinkedIn.</p>

[<img align="left" alt="FouzanAkhter | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin]
[<img align="left" alt="FouzanAkhter | X (formerly Twitter)" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@12.1.0/icons/x.svg" />][x]
[<img align="left" alt="FouzanAkhter | GitHub" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@12.1.0/icons/github.svg" />][github]
[<img align="left" alt="FouzanAkhter | Upwork" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@12.1.0/icons/upwork.svg" />][upwork]

[linkedin]: https://www.linkedin.com/in/fouzan-akhter/
[x]: https://github.com/fouzan-akhter
[github]: https://github.com/fouzan-akhter
[upwork]: https://www.upwork.com/freelancers/~019789c3a540248cea
