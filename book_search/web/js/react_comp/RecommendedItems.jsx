import React, { Component } from 'react';
class Recommended extends Component {
    render()
    {
        let output_text = this.props.processed_text

        console.log("Greetings from recommender engine " + output_text)
        return(
            <div>
                <div dangerouslySetInnerHTML={{__html: output_text}} />
            </div>
       )
    }
}

export default Recommended
