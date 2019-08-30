import React, { Component } from 'react';

export default class GetUserInput extends Component {
    render()
    {

        const element = (
            <div>
              <form onSubmit={this.handleSubmit}>
              <table>
                <tr>
                    <td>
                        <textarea id="input_textarea" rows = "1" cols = "30"></textarea>
                    </td>
                </tr>
                <tr align="center">
                  <input type="submit" value="Search Bookes"/>
                </tr>
              </table>
              </form>
            </div>
        );
        return element
    }
}