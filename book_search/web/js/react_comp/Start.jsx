import React, { Component } from 'react';
import TitleHeader from './TitleHeader'
import GetUserInput from './GetUserInput'
import Recommended from './RecommendedItems'
import TableDisplay from './TableDisplay'

export default class Start extends Component {
    constructor(props) {
        super(props);
        this.set_proceesed_text = this.set_proceesed_text.bind(this);
        this.state = {processed_text: '[{"name": "", "author": "", "yop": "", "publisher": "", "isbn": "", "ratings": ""}]'};
    };

    set_proceesed_text(text){
        return this.setState({processed_text : text});
    }

    render()
    {
        let root = document.getElementById('contents');
        let url = root.getAttribute('data-url')
        let port = root.getAttribute('data-port')
        let items = root.getAttribute('data-items')

        console.log(url)

        const element = (
            <table>
                <tbody>
                    <tr align="centre">
                        <td>
                            <TitleHeader />
                            <GetUserInput url={url} port={port} homeCallBack={this.set_proceesed_text}/>
                            <TableDisplay processed_text={this.state.processed_text} />
                        </td>
                    </tr>
                </tbody>
            </table>
        );
        return element
    }
}