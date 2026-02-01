import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';

function App() {
    return (
        <Router>
            <div className="App">
                <h1>Welcome to the Octofit Tracker</h1>
                <Switch>
                    {/* Define your routes here */}
                    <Route path="/" exact>
                        <h2>Home Page</h2>
                    </Route>
                    {/* Add more routes as needed */}
                </Switch>
            </div>
        </Router>
    );
}

export default App;