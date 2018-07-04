

import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class CollegeList extends Component {

    state ={
        collegesList : []
    }
    componentDidMount(){

        fetch('http://127.0.0.1:8000/api/v2/colleges/')
        .then(response => response.json())
        .then(responseJson => {
        this.setState({ collegesList : responseJson});
        })
        .catch(e => {console.log ("Error");});
    }


    render(){
    return(
        <React.Fragment>
            <div className="container">
                <table className="table table-bordered">
                    <thead>
                        <th>Acronym</th>
                        <th>College Name</th>
                        <th>Location</th>
                        <th>Contact</th>
                    </thead>
                    <tbody>
                    {this.state.collegesList.map(item => (
                        <tr key={item.id}>
                            <td>{item.Name}</td>
                            <td><Link to={'/colleges/' + item.id}>{item.Acronym}</Link></td>
                            <td>{item.Location}</td>
                            <td>{item.Contact}</td>
                        </tr>

                    ))}
                    </tbody>

                </table>
            </div>
        </React.Fragment>
        );
    }
}

export default CollegeList

