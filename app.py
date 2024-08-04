from flask import Flask, render_template, request, jsonify
import threading
import time
import pyautogui

app = Flask(__name__)

# Flag to control the execution of the pyautogui automation
stop_flag = False

topics = [
    "virtual environment", "Basic Git commands", "SQL join types",
    "JavaScript debugging", "Docker introduction", "REST vs. SOAP API",
    "Front-end vs. back-end", "JavaScript async/await", "CSS Flexbox",
    "Node.js and npm installation", "Python list comprehensions",
    "Python unit testing", "Responsive web design", "Environment variables",
    "JavaScript event listeners", "TypeScript introduction", "SQL queries",
    "HTML5 features", "Python decorators", "JavaScript promises",
    "React components", "Vue.js basics", "Angular directives",
    "Microservices architecture", "CI/CD pipelines", "Kubernetes basics",
    "GraphQL introduction", "NoSQL databases", "Web security fundamentals",
    "OAuth2.0 authorization", "Webpack configuration", "Bash scripting",
    "Linux command line", "Software testing strategies", "Agile methodologies",
    "Project management tools", "Cloud computing fundamentals",
    "Machine learning basics", "Data visualization with Python"
]

def search_in_browser():
    global stop_flag
    stop_flag = False
    time.sleep(3)
    pyautogui.hotkey('win', '1')  # Open Edge browser (adjust if needed)

    pyautogui.hotkey('ctrl', 't')
    time.sleep(2)
    pyautogui.write('https://rewards.bing.com/?signin=1&FORM=ANNRW1')
    pyautogui.press('enter')
    time.sleep(5)

    for i in range(len(topics)):
        if stop_flag:
            break

        if i > 0:
            pyautogui.hotkey('ctrl', 't')
            time.sleep(2)
            pyautogui.write('site:www.geeksforgeeks.org ' + topics[i])
            pyautogui.press('enter')
            time.sleep(3)

            # Do not close the browser, only close the tabs
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1)

    return "PASS"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_search():
    global stop_flag
    stop_flag = False
    threading.Thread(target=search_in_browser).start()
    return jsonify({'status': 'started'})

@app.route('/stop', methods=['POST'])
def stop_search():
    global stop_flag
    stop_flag = True
    return jsonify({'status': 'stopped'})

if __name__ == '__main__':
    app.run(debug=True)
