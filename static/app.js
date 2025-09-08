import { marked } from "./marked.esm.js"

const fetch_message = async (message) => {
    const post_data = {
       "message": message 
    }

    const response = await fetch("/api/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(post_data)
    })
    const data = await response.json()

    return data
}

function create_chats(message, incomming = true) {
    const message_container = document.createElement("div")
    message_container.classList.add(
        "message", incomming ? "incomming" : "outcomming"
    )
    message_container.innerHTML = message
    
    return message_container
}

const prompt_form = document.getElementById("prompt_form")

prompt_form.onsubmit = async (e) => {
    e.preventDefault()
    const incomming_chat = create_chats(prompt_form.children[0].value)

    const data = await fetch_message()
    const outcomming_chat = create_chats(data.message, false)

    const messages_container = document.querySelector(".messages_container")

    messages_container.appendChild(incomming_chat)
    messages_container.appendChild(outcomming_chat)


}


const prompt_field = prompt_form.children[0]

prompt_field.addEventListener("input", () => {
    const trimmed_value = prompt_field.value.trim()
    if (trimmed_value.length > 0) {
        prompt_form.children[1].removeAttribute("disabled")
    } else {
        prompt_form.children[1].setAttribute("disabled", "")
    }

})

