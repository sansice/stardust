import React, { Component } from 'react';
import TitleHeader from './TitleHeader'
import GetUserInput from './GetUserInput'

export default class Start extends Component {
    render()
    {

        const element = (
        <table>
            <tbody>
                <tr align="centre">
                    <td>
                        <TitleHeader />
                        <GetUserInput />
                    </td>
                </tr>
            </tbody>
        </table>
        );
        return element
    }
}