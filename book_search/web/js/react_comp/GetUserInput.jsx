import React, { Component } from 'react';

export default class GetUserInput extends Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.homeCallBack = props.homeCallBack
    }

    handleSubmit(event) {

        let input_text = document.getElementById("input_textarea").value;
        input_text = input_text.replace(/\n/g, " ");
        input_text = input_text.replace(/[^0-9a-zA-Z]/g, " ");
        let proceesed_text = [];
        console.log("The text area data is captured");
        console.log(this.props.homeCallBack)
        fetch("http://"+this.props.url+":"+this.props.port+"/process?search_text=" + input_text).then(function (response) {
            console.log(response);
            return response.text();

        }).then(function (text) {
            console.log("The text is " + text);
            this.props.homeCallBack(text)
        }.bind(this));
        console.log("Text is " + proceesed_text)

        event.preventDefault();
    }

    render()
    {

        const element = (
            <div>
              <form onSubmit={this.handleSubmit}>
              <table>
                <tbody>
                    <tr>
                        <td>
                            <textarea id="input_textarea" rows = "1" cols = "30"></textarea>
                        </td>
                    </tr>
                    <tr align="center">
                        <td>
                            <input type="submit" value="Search Bookes"/>
                         </td>
                    </tr>
                </tbody>
              </table>
              </form>
            </div>
        );
        return element
    }
}