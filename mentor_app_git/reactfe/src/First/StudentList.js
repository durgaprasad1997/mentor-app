

import React, { Component } from 'react';

class StudentList extends Component {

    state ={
        studentList : []

    }
    componentDidMount(){
        fetch('http://127.0.0.1:8000/api/v2/colleges/' + this.props.match.params.id + '/students/')
        .then(response => response.json())
        .then(responseJson => {
        this.setState({ studentList : responseJson});
        })
        .catch(e => {console.log (e);});
    }


    render(){
    return(
        <React.Fragment>
            <div>
                <table>
                    <thead>
                        <th>Name</th>
                        <th>Db Name</th>
                        <th>Email</th>
                    </thead>
                    <tbody>
                    {this.state.studentList.map(item => (
                        <tr key={item.id}>
                            <td>{item.Name}</td>
                            <td>{item.Dbnames}</td>
                            <td>{item.Email_id}</td>
                        </tr>

                    ))}
                    </tbody>

                </table>
            </div>
        </React.Fragment>
        );
    }
}

export default StudentList