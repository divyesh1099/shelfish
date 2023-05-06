import React, { Component } from "react"

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      available: true,
      activeItem: {
        title: "",
        available: false
      },
      bookList: []
      };
  }

    async componentDidMount() {
      try {
        const res = await fetch('http://localhost:8000/booksapi/books/');
        const bookList = await res.json().results;
        this.setState({
          bookList
        });
      } catch (e) {
        console.log(e);
    }
    }
    renderItems = () => {
      const newItems = this.state.bookList;
      return newItems.map(item => (
        <li 
          key={item.id}
          className="list-group-item d-flex justify-content-between align-items-center"
        >
          <span 
            className={`todo-title mr-2 ${
              this.state.available ? "available-todo" : ""
            }`}
            title={item.title}
            >
              {item.title}
            </span>
        </li>
      ));
    };

    render() {
      return (
        <main className="content">
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <ul className="list-group list-group-flush">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
      )
    }
  }
  
export default App;