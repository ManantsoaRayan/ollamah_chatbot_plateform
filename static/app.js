import { marked } from "./marked.esm.js"

let current_outcomming_message = null
let event_source

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
    // prevent from reloading
    e.preventDefault()
    const prompt = prompt_form.children[0].value
    const incomming_chat = create_chats(prompt)

    const messages_container = document.querySelector(".messages_container")
    messages_container.appendChild(incomming_chat)

    const encoded_prompt = encodeURIComponent(prompt)
    event_source = new EventSource(`/api/generate?prompt=${encoded_prompt}`)

    current_outcomming_message = create_chats("", false)
    messages_container.appendChild(current_outcomming_message)

    event_source.onmessage = (e) => {
        const text = JSON.parse(e.data)
        current_outcomming_message.innerHTML += text
    }

    event_source.addEventListener("done", () => {
        current_outcomming_message.innerHTML = marked.parse(current_outcomming_message.textContent)
        current_outcomming_message = null
        event_source.close()
    })
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

