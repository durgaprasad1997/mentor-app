import React, { Component } from 'react';

class CollegeList extends Component {

    state ={
        collegesList : []
    }
    componentDidMount(){
        fetch('http://127.0.0.1:8000/onlineapp/api/v2/colleges/')
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
                        <th>College</th>
                        <th>College Acronym</th>
                        <th>Location</th>
                        <th>Contact</th>
                    </thead>
                    <tbody>
                    {this.state.collegesList.map(item => (
                        <tr key={item.id}>
                            <td>{item.Name}</td>
                            <td>{item.Acronym}</td>
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