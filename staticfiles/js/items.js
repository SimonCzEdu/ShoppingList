const editButtons = document.getElementsByClassName("btn-edit");
const itemText = document.getElementById("id_item_name");
const itemForm = document.getElementById("itemForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated items's ID upon click.
 * - Fetches the content of the corresponding item.
 * - Populates the `itemText` input/textarea with the item's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_item/{itemId}` endpoint.
 */

for (let button of editButtons) {
    button.addEventListener('click', (e) => {
        let itemId = e.target.getAttribute("item_id");
        let itemContent = document.getElementById(`item${itemId}`).innerText;
        console.log('click')
        itemText.value = itemContent;
        submitButton.innerText = "Update";
        itemForm.setAttribute("action", `edit_item/${itemId}`);
    });
}


/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated item's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific item.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let itemId = e.target.getAttribute("item_id");
        deleteConfirm.href = `delete_item/${itemId}`;
        deleteModal.show();
    });
}