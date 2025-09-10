import { marked } from "./marked.esm.js"

let current_outcomming_message = null
let event_source

async function get_session() {
    try {
        const response = await fetch("/session/all", {
            method: "POST",
            headers: { "Content-Type": "application/json" }
        })
        return await response.json()
    }
    catch (e) {
        console.log(e)
        alert("failed to load session. Reload the page")
    }
}

window.onload = async () => {
    const sessions = (await get_session()).body
    sessions.forEach( (session) => {
        const session_card = document.createElement("div")
        session_card.classList.add("nav_item")
        session_card.textContent = session.session_name
        session_card.setAttribute("id", session.id.toString())

        document.querySelector(".nav_items").appendChild(session_card)
    })

};

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
        current_outcomming_message.textContent += text
    }

    event_source.addEventListener("done", () => {
        current_outcomming_message.innerHTML = marked.parse(current_outcomming_message.textContent)
        current_outcomming_message = null
        event_source.close()
    })

    prompt_form.children[0].value = ""
}

function bind_inputs_to_button(form, input, submitter) {
    const trimmed_value = input.trim()
    if (trimmed_value.length > 0) {
        form.children[submitter].removeAttribute("disabled")
    } else {
        form.children[submitter].setAttribute("disabled", "")
    }
}

const prompt_field = prompt_form.children[0]

prompt_field.addEventListener("input", () => bind_inputs_to_button(prompt_form, prompt_field.value, 1))

// popup dialog -------------------------------------------------

const popupDialog = document.getElementById("popup_dialog")


const dialog_controllers = document.querySelectorAll(".dialog_controller")

dialog_controllers.forEach(controller => {
    controller.onclick = () => popupDialog.classList.toggle("show")
})


popupDialog[0].oninput = () => bind_inputs_to_button(popupDialog, popupDialog[0].value, 1)

popupDialog.onsubmit = async e => {
    e.preventDefault()

    const session_name = popupDialog.children[0].value

    const name_is_valid = session_name.trim().length > 0 

    if (!name_is_valid){
        alert("field must be completed")
        return false
    }

    // get response if there are errors
    const response = await fetch("/session/create", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({session_name})
    })

    
    const data = await response.json()

    if ( data.status == "failure") {
        alert(`creation failed: ${data.error}`)
    } else {
        
    }

    popupDialog.children[0].value = ""
    popupDialog.classList.toggle("show")

}
