from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample initial data
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is not None:
        return jsonify({'task': task})
    else:
        return jsonify({'message': 'Task not found'}, 404)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' in data:
        new_task = {'id': len(tasks) + 1, 'title': data['title']}
        tasks.append(new_task)
        return jsonify({'message': 'Task created', 'task': new_task})
    else:
        return jsonify({'message': 'Title is required'}, 400)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is not None and 'title' in data:
        task['title'] = data['title']
        return jsonify({'message': 'Task updated', 'task': task})
    else:
        return jsonify({'message': 'Task not found or title is missing'}, 404)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is not None:
        tasks.remove(task)
        return jsonify({'message': 'Task deleted'})
    else:
        return jsonify({'message': 'Task not found'}, 404)

if __name__ == '__main__':
    app.run(debug=True)
