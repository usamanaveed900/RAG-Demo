from flask import Flask, request, render_template_string

class RAGApp:
    def __init__(self, chatbot):
        self.chatbot = chatbot
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        """Define routes for the Flask app."""
        html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>RAG Chatbot</title>
            <style>
                /* Global Styles */
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f9;
                }

                /* Navigation Bar */
                nav {
                    display: flex;
                    align-items: center;
                    /* justify-content: space-between; */
                    /* padding: 5px 10px; */
                    padding-top: 5px;
                    padding-right: 15px;
                    padding-bottom: 5px;
                    padding-left: 10px;
                    background-color: #007bff;
                    color: white;
                }
                nav img {
                    height: 60px;
                }
                nav .title {
                    font-size: 1em;
                    font-weight: bold;
                }

                /* Main Content */
                .container {
                    max-width: 800px;
                    margin: 50px auto;
                    background: white;
                    padding: 20px;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                }
                h1 {
                    text-align: center;
                    color: #333;
                }
                p {
                    text-align: center;
                    color: #333;
                }

                form {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }
                input[type="text"] {
                    width: 80%;
                    padding: 10px;
                    margin: 20px 0;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    font-size: 16px;
                }
                button {
                    padding: 10px 20px;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                }
                button:hover {
                    background-color: #0056b3;
                }

                /* Response Section */
                .response {
                    margin-top: 20px;
                    padding: 15px;
                    border: 1px solid #007bff;
                    border-radius: 4px;
                    background-color: #f0f8ff;
                    font-size: 16px;
                    color: #333;
                }
            </style>
        </head>
        <body>
            <nav>
                <div>
                    <img src="/static/Logo.png" alt="RAG Logo">
                </div>
                <div class="title">RAG Demo</div>
            </nav>
            <div class="container">
                <h1>Chatbot</h1>
                <p>Retrieval-Augmented Generation - Demo</p>
                <form method="POST">
                    <input type="text" id="query" name="query" placeholder="Enter your query here..." required>
                    <button type="submit">Ask</button>
                </form>
                {% if response %}
                    <div class="response">
                        <strong>Response:</strong>
                        <p>{{ response }}</p>
                    </div>
                {% endif %}
            </div>
        </body>
        </html>
        """

        @self.app.route("/", methods=["GET", "POST"])
        def chatbot():
            response = None
            if request.method == "POST":
                query = request.form["query"]
                response = self.chatbot.get_response(query)
            return render_template_string(html_template, response=response)

    def run(self):
        """Run the Flask app."""
        self.app.run(debug=True)
