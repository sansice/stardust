import React from 'react';
import { HashRouter, Route, hashHistory } from 'react-router-dom';
import Start from './react_comp/Start';
// import more components
export default (
    <HashRouter>
     <div>
      <Route path='/' component={Start} />
     </div>
    </HashRouter>
);