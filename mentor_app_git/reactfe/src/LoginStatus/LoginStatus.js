import React, { Component } from 'react';

class Header extends Component {

    state={
        isLoggedIn: this.props.isLoggedIn
    }

    toggleLoggedIn = () =>{
        this.setState(prev=>({isLoggedIn: !prev.isLoggedIn}))
    }

    render() {

        const {title} = this.props;
        const {isLoggedIn} = this.state;

        return(

            <div>
                <h2>{title}</h2>

                <div onClick = {this.toggleLoggedIn}>{

                    isLoggedIn ?<span>Logout</span> : <span>Login</span>

                }
                </div>
            </div>

        )
  }
}

export default Header;
