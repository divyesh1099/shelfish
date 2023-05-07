const getBooks = async () => {
        const response = await fetch('http://localhost:8000/booksapi/books');
        const myJson = await response.json();
        const books = myJson.results;
        console.log(books);
        const booksDiv = document.getElementById('books');
        const viewBooksButton = document.getElementById('viewBooks');
        viewBooksButton.classList.add('hide')
        for(let i=0; i < books.length; i++){
            var to_do = "Borrow"
            if(books[i].availability == 'borrowed'){
                to_do = "Return"
            }
            booksDiv.innerHTML += `
            <div class="row m-1 p-1">
                <div class="col-sm-6 mb-3 mb-sm-0">
                    <div class="card" id="bookCard-${books[i].id}">
                    <div class="card-body">
                        <h5 class="card-title">${books[i].title}</h5>
                        <p class="card-text">${books[i].availability}</p>
                        <a href="#" onclick='borrow_return(${books[i].id}, "${books[i].title}", "${books[i].availability}")' class="btn btn-primary">
                        ${to_do}
                        </a>
                        <a class="btn btn-warning" href="#" onclick="edit(${books[i].id})">Edit Book</a>
                        <a class="btn btn-danger" href="#" onclick="deleteBook(${books[i].id})">Delete Book</a>
                        
                    </div>
                    </div>
                </div>
            <div>
            `
        }
    }

const borrow_return = async (id, title, availability) => {
    if(isLoggedIn()){
        if(availability == 'available'){
            fetch("http://localhost:8000/booksapi/books/" + id + "/", {
                method: "PUT",
                
                body: JSON.stringify({
                    title: title,
                    availability: "borrowed"
                }),
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
            });
            alert('Book Borrowed');
        } else {
            fetch("http://localhost:8000/booksapi/books/" + id + "/", {
                method: "PUT",
                
                body: JSON.stringify({
                    title: title,
                    availability: "available"
                }),
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
            });
            alert('Book Returned');
        }
    }
    else{
        window.location.href = "./login.html";
    }
}

const edit = async(id) =>{
    if(isLoggedIn()){
        const bookCard = document.getElementById('bookCard-'+ id);
        const response = await fetch('http://localhost:8000/booksapi/books/' + id + '/');
        const book = await response.json();
        bookCard.innerHTML += `
        <div class="editBookForm">
            <div class="card m-1 p-3">
                <div class="card-body">
                    <label for="bookTitle">Title</label>
                    <input type="text" name="bookTitle" class="form-control" id="editedBookTitle" value="${book.title}" required placeholder="Enter Book Title Here">
                </div>
                <div class="card-footer">
                    <button onclick="saveEditedBook(${book.id}, '${book.title}')" class="m-1 btn btn-success" id="editBook">Save Edited Book</button>
                </div>
            </div>                        
        </div>
        `
    } else {
        window.location.href = './login.html';
    }
}

const saveEditedBook = async(id)=>{
    var editedBookTitle = document.getElementById('editedBookTitle');

    fetch("http://localhost:8000/booksapi/books/" + id + "/", {
            method: "PUT",
            
            body: JSON.stringify({
                title: editedBookTitle.value,
                availability: "available"
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
    });
}

const createBook = async(title) =>{
    if(isLoggedIn()){

        var bookTitleInput = document.getElementById('bookTitle');
        
        fetch("http://localhost:8000/booksapi/books/", {
                method: "POST",
                
                body: JSON.stringify({
                    title: bookTitleInput.value,
                    availability: "available"
                }),
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
            });
            alert('Book Created');
    } else {
        window.location.href = './login.html';
    }
}

const deleteBook = async(id) => {
    if(isLoggedIn()){
        fetch("http://localhost:8000/booksapi/books/" + id + "/", {
                method: "DELETE",
            });
        alert("Book Deleted Successfully.")
    } else {
        window.location.href = './login.html';
    }
}

function EnableDisable(txtPassportNumber) {
    //Reference the Button.
    var btnSubmit = document.getElementById("createBook");

    //Verify the TextBox value.
    if (txtPassportNumber.value.trim() != "") {
        //Enable the TextBox when TextBox has value.
        btnSubmit.disabled = false;
    } else {
        //Disable the TextBox when TextBox is empty.
        btnSubmit.disabled = true;
    }
};

const isLoggedIn = () => {
    var jwt = sessionStorage.getItem('jwt');
    if(jwt){
        var loginButton = document.getElementById('loginButton');
        var registerButton = document.getElementById('registerButton');
        var logoutButton = document.getElementById('logoutButton');
        loginButton.classList.add('hide');
        registerButton.classList.add('hide');
        logoutButton.classList.remove('hide');
        getUserIfLoggedIn(jwt);
        return true;
    } else {
        return false
    }
}

function getUserIfLoggedIn(jwt){

}

document.addEventListener('DOMContentLoaded', function() {
    isLoggedIn();
    var main = document.getElementById('main');
    main.innerHTML += `
    <button class="btn btn-success" onclick="createNewBookForm()">Create New Book</button>
    <div id="createNewBook"></div>
    `
}, false);

const logout = async() =>{
    fetch("http://localhost:8000/users/logout", {
            method: "POST",
        });
    sessionStorage.removeItem('jwt');
    var loginButton = document.getElementById('loginButton');
    var registerButton = document.getElementById('registerButton');
    var logoutButton = document.getElementById('logoutButton');
    logoutButton.classList.add('hide');
    loginButton.classList.remove('hide');
    registerButton.classList.remove('hide');
    alert("Logged Out Successfully");
    window.location.href = './login.html';
}

function createNewBookForm(){
    var createNewBookFormDiv = document.getElementById('createNewBook')
    createNewBookFormDiv.innerHTML += `
    <div class="card m-1 p-3">
        <div class="card-body">
            <label for="bookTitle">Title</label>
            <input type="text" name="bookTitle" onkeyup="EnableDisable(this)" class="form-control" id="bookTitle" required placeholder="Enter Book Title Here">
        </div>
        <div class="card-footer">
            <button onclick="createBook()" class="m-1 btn btn-success" id="createBook" disabled="disabled">Create a New Book</button>
        </div>
    </div>
    `
}