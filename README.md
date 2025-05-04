# 🧠 CodeSage: AI-Powered Code Review Assistant  

A local, privacy-respecting AI assistant that reviews your code using DeepSeek-Coder via Ollama. Features an API backend (FastAPI) and a clean Streamlit interface for effortless code analysis and suggestions.

## 🌟 Why CodeSage?

CodeSage empowers developers by providing instant, intelligent code reviews locally. It ensures privacy, speed, and accuracy, making it an essential tool for improving code quality without relying on external services.

[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?style=flat&logo=streamlit)](https://streamlit.io/)  
[![License](https://img.shields.io/github/license/yourusername/code-review-assistant?style=flat)](LICENSE)  

> A local AI-powered assistant for reviewing source code using the DeepSeek-Coder model and Ollama. Designed for developers who want quick, intelligent feedback on their code from a locally hosted LLM.

---

## 📌 Short Description

A local, privacy-respecting AI assistant that reviews your code using DeepSeek-Coder via Ollama. Features an API backend (FastAPI) and a clean Streamlit interface for effortless code analysis and suggestions.

---

## 📘 Detailed Description

CodeSage is an intelligent, developer-friendly code review assistant that uses the power of large language models (LLMs) — specifically DeepSeek-Coder, hosted locally via Ollama — to analyze your code and provide meaningful, human-like reviews.

Designed for individual developers, teams, and learners, CodeSage helps you:

- Identify bugs or anti-patterns  
- Improve code readability  
- Get optimization and best-practice suggestions  
- Learn from AI-powered senior code insights  

CodeSage is privacy-friendly (no cloud dependencies), runs entirely locally, and can be used via:

- A FastAPI backend that exposes a simple review API (`/review/`)  
- A lightweight Streamlit frontend where users can paste and submit code easily  

---

## ✅ Use Case Scenarios

- Software developers wanting on-demand code insights  
- Bootcamp students or beginners learning coding best practices  
- Teams needing quick, local reviews during development  
- Offline environments or air-gapped systems  

---

## 🚀 Features

- ✅ Review any code snippet and get feedback.  
- 🧠 Uses DeepSeek-Coder via Ollama.  
- ⚡ FastAPI backend for API integration.  
- 🎨 Streamlit frontend for an easy-to-use UI.  
- 📦 Lightweight, fast, and customizable.  
- 🔒 Fully local processing for enhanced privacy.  
- 📊 Detailed feedback with actionable suggestions.  

---

## 📁 Project Structure

```
code-review-deepseek/
├── backend/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── .gitignore
├── docker-compose.yml
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

---

## 🔧 Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/code-review-assistant.git
   cd code-review-assistant
   ```

2. **Install dependencies**  
   - Backend:  
     ```bash
     cd backend
     pip install -r requirements.txt
     ```
   - Frontend:  
     ```bash
     cd frontend
     pip install -r requirements.txt
     ```

3. **Run Ollama**  
   Ensure Ollama is installed and running locally.

4. **Start the backend and frontend**  
   - Backend:  
     ```bash
     uvicorn main:app --reload
     ```
   - Frontend:  
     ```bash
     streamlit run app.py
     ```

---

## ⚙️ API Usage

### Endpoint:  
`POST /review/`  

### Example Payload:  
```json
{
  "code": "<your-code>"
}
```

### Example Response:  
```json
{
  "feedback": "Your code is well-structured, but consider adding type hints for better readability."
}
```

---

## 🔐 Configuration

- Copy `.env.example` to `.env` and update the necessary environment variables.  
- Ensure all required dependencies are installed.  

---

## 🖼️ Screenshots

*(Add input/output screenshots here.)*

---

## 🛠️ Development Workflow

1. **Fork the repository**  
   Create your own copy of the repository by forking it.

2. **Create a new branch**  
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**  
   Implement your feature or fix.

4. **Run tests**  
   Ensure all tests pass before committing.  

5. **Commit your changes**  
   ```bash
   git commit -m "Add your commit message here"
   ```

6. **Push your changes**  
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a pull request**  
   Submit your changes for review.

---

## 🧪 Testing

- Run unit tests for the backend:  
  ```bash
  pytest
  ```
- Run integration tests for the frontend:  
  *(Add specific commands if applicable)*  

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

<div align="center">

[![GitHub WidgetBox](https://github-widgetbox.vercel.app/api/profile?username=Hardik-Sankhla&data=followers,repositories,stars,commits&theme=dracula)](https://github.com/Hardik-Sankhla/)

**Hardik Sankhla**  
🎓 Data Science Student - AI & ML Engineer | 🌟 Open Source Contributor | Oracle Certified OCI Generative AI Professional | OCI Foundation Associate | OCI DATA Associate | OCI AI Associate 



<div align="center">
  <a href="https://www.youtube.com/">
    <img src="https://img.shields.io/static/v1?message=Youtube&logo=youtube&label=&color=FF0000&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="YouTube logo" />
  </a>
  <a href="https://twitter.com/hardik_sankhla">
    <img src="https://img.shields.io/static/v1?message=Twitter&logo=twitter&label=&color=1DA1F2&logoColor=white&labelColor=&style=for-the-badge" height="25" alt="Twitter logo" />
  </a>
</div>

<p align="center">
  <a href="https://linkedin.com/in/hardik-sankhla"><img src="https://img.shields.io/badge/LinkedIn-Hardik%20Sankhla-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"></a>
  <a href="https://github.com/Hardik-Sankhla"><img src="https://img.shields.io/badge/GitHub-Hardik%20Sankhla-black?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="mailto:datascientist.hardiksankhla@email.com"><img src="https://img.shields.io/badge/Email-datascientist.hardiksankhla%40email.com-red?style=for-the-badge&logo=gmail" alt="Email"></a>
  <a href="https://dataxhardik.wixsite.com/myportfolio"><img src="https://img.shields.io/badge/Portfolio-Hardik%20Sankhla-ff69b4?style=for-the-badge&logo=appveyor" alt="Portfolio"></a>
</p>

📝 [PeerList](https://peerlist.io/hardiksankhla) | ✉️ [Email Me](mailto:datascientist.hardikSankhla@gmail.com)

</div>

<br>

<p align="left">I'm Hardik Sankhla from Jodhpur, I am a passionate software developer with a keen interest in building scalable and efficient applications. I enjoy working with modern web technologies and continuously learning new things to enhance my skills. <br><br>

- 🔭 I’m working as AI Intern at Gyan Netra<br>
- 📚 I'm currently learning Generative AI <br>
- ⚡ In my free time, I explore AI Agents & Agentic AI<br>
- 🎓 Data Science student at JIET Institute of Design and Technology<br>
- 💼 Skilled in Data Analytics, Visualization, ML, and Cloud Computing<br>
- 💡 Eager to contribute innovative solutions in both Data Science and Cloud domains<br>
- 🌱 Currently learning advanced concepts in Deep Learning
</p>

---

## 🤝 Contribution

We welcome contributions from the community! Follow the development workflow above to get started.  

---

## 📬 Contact

Created by Hardik Sankhla — [LinkedIn](https://linkedin.com/in/hardik-sankhla)  

For any queries or issues, feel free to open an issue or reach out via email.

---

## 🌐 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)  
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [Ollama Documentation](https://ollama.ai/)  

---

## 🏗️ Future Enhancements

- Add support for multiple programming languages.  
- Implement advanced customization options for feedback.  
- Integrate with popular IDEs like VS Code and PyCharm.  
- Add CI/CD pipelines for automated testing and deployment.  

---

## ⭐ Acknowledgments

Special thanks to the open-source community and contributors who made this project possible.
