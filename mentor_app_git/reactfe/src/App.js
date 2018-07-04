import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import CollegeList from './First/CollegeList';
import Header from './LoginStatus/LoginStatus';
import StudentList from './First/StudentList';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";


class App extends Component {
  render() {
    return (
      <div className="App">
        <Header/>
        <React.Fragment>
            <Router>
                <div>
                    <Route exact path="/" component = {CollegeList}/>
                    <Route exact path="/rcolleges/:id/" component = {StudentList}/>

                </div>
            </Router>
        </React.Fragment>
      </div>
    );
  }
}

export default App;















//import React, { Component } from 'react';
//import logo from './logo.svg';
//import './App.css';
//
//import Header from './LoginStatus/LoginStatus';
//import CollegeList from './JsonResponse/JsonResponse';
//
//import App from './First/App';
//
//
//class App extends Component {
//  render() {
//    return (
//      <div className="App">
//        <header className="App-header">
//          <h1 className="App-title">Welcome to Onlineapp</h1>
//            <Header/>
//
//        </header>
//        <App/>
//   // <CollegeList/>
//      </div>
//    );
//  }
//}
//
//export default App;
