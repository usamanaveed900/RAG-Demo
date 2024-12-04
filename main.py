from retriever import Retriever
from generator import Generator
from chatbot import RAGChatbot
from app import RAGApp
import os


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


if __name__ == "__main__":
    # 1. Define documents
    documents = [
            "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines designed to think like humans. These machines can perform tasks like learning, problem-solving, and decision-making.",
            "Machine Learning (ML) is a subset of AI that involves the use of algorithms to allow machines to learn from data. ML models improve their performance over time with more data, making them capable of tasks like image recognition and language translation.",
            "Deep Learning is a type of machine learning that uses neural networks with many layers (hence 'deep'). It has been highly effective in areas like image and speech recognition, as well as natural language processing.",
            "Natural Language Processing (NLP) is a branch of AI that focuses on enabling machines to understand, interpret, and generate human language. It powers applications like chatbots, translators, and sentiment analysis.",
            "Reinforcement Learning (RL) is an area of machine learning where an agent learns to make decisions by performing actions and receiving feedback in the form of rewards or penalties. It has applications in robotics, gaming, and autonomous vehicles.",
            "Supervised Learning is a type of machine learning where the algorithm is trained on labeled data. The model learns to map input to the correct output based on the examples in the training set.",
            "Unsupervised Learning is another machine learning method where the model is trained on data without labels. It finds patterns and structures in the data, often used for clustering or anomaly detection.",
            "AI ethics is a field of study that focuses on the moral implications of AI technologies. It includes concerns about bias, privacy, accountability, and the societal impacts of AI systems.",
            "A neural network is a computational model inspired by the way biological neurons work. Neural networks are used in many AI applications, including image and speech recognition, as well as in decision-making systems.",
            "Computer Vision is a subfield of AI focused on enabling machines to interpret and understand visual information from the world. It is widely used in industries like healthcare, automotive, and entertainment.",
            "AI in healthcare involves using machine learning algorithms and AI technologies to improve patient care, diagnosis, and treatment planning. AI-powered systems can analyze medical images, predict disease risks, and assist doctors in decision-making.",
            "The Turing Test is a concept introduced by Alan Turing to determine whether a machine can exhibit intelligent behavior indistinguishable from that of a human. It remains a foundational idea in AI philosophy.",
            "AI-powered chatbots use natural language processing (NLP) to simulate conversations with humans. They are used in customer service, education, and various industries to interact with users and provide information.",
            "Autonomous vehicles use a combination of AI, sensors, and machine learning to drive without human intervention. AI allows these vehicles to understand their environment, make decisions, and navigate safely on the roads.",
            "The AI Winter refers to periods in the history of artificial intelligence where progress slowed, and funding for AI research decreased due to unmet expectations. These periods have historically been followed by bursts of innovation when new techniques or breakthroughs occur.",
            "Generative AI is a subset of AI focused on creating new content such as images, videos, music, and text. It uses machine learning models like GANs (Generative Adversarial Networks) to generate novel outputs based on input data.",
            "Explainable AI (XAI) refers to methods and techniques in AI that make the decisions and actions of machine learning models understandable by humans. This is particularly important in high-stakes fields like healthcare and law.",
            "AI-driven recommendation systems are used by companies like Amazon, Netflix, and YouTube to provide personalized recommendations to users based on their previous behavior and preferences. These systems rely on data analysis and machine learning.",
            "The concept of Artificial General Intelligence (AGI) refers to AI systems that possess the ability to understand, learn, and apply intelligence across a wide range of tasks, similar to human cognitive abilities. AGI is still a theoretical concept and has not yet been realized.",
            "Neural machine translation (NMT) is a type of machine translation that uses deep learning to translate text from one language to another. It has significantly improved the accuracy and fluency of translations compared to traditional statistical methods.",
            "AI-powered robots are being used in various industries for tasks ranging from assembly line work to complex surgery. These robots use machine learning and computer vision to perform tasks autonomously or assist human operators.",
            "Cognitive computing is a branch of AI that mimics human thought processes in analyzing complex data. It aims to create systems that can solve problems and make decisions in a way that resembles human cognition, often used in healthcare, finance, and business analytics."
        ]

    # 2. Initialize components
    retriever = Retriever(documents)
    generator = Generator(openai_key="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")  # Replace with your OpenAI API key

    # 3. Create RAG chatbot
    chatbot = RAGChatbot(retriever, generator)

    # 4. Launch Flask app
    app = RAGApp(chatbot)
    app.run()
