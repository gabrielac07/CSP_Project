const taskInput = document.getElementById("taskInput");
const addTaskButton = document.getElementById("addTaskButton");
const taskList = document.getElementById("taskList");

let tasks = [];

addTaskButton.addEventListener("click", () => {
    const taskDescription = taskInput.value.trim();

    if (taskDescription) {
        const task = { description: taskDescription, status: "In Progress" };
        tasks.push(task);
        taskInput.value = "";
        renderTasks();
    }
});

function renderTasks() {
    taskList.innerHTML = "";
    tasks.forEach((task, index) => {
        const li = document.createElement("li");
        li.innerHTML = `
            ${task.description} - ${task.status} 
            <button onclick="completeTask(${index})">Complete</button>
        `;
        taskList.appendChild(li);
    });
}

function completeTask(index) {
    tasks[index].status = "Completed";
    renderTasks();
}
