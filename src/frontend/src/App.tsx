import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { createGlobalStyle } from 'styled-components';
import { COLOR_LIGHT_GREY, COLOR_TEAL } from './constants';
import Header from './components/header/Header';
import Body from './components/Body';
import Footer from './components/Footer';

const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    color: ${COLOR_LIGHT_GREY};
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
      'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
      sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  a {
    color: ${COLOR_TEAL};
    text-decoration: none;
  }
  ul {
    list-style-type: none;
    padding-inline-start: 0;
  }
`;

const App: React.FC = () => {
  return (
    <div className="App">
      <GlobalStyle />
      <Router>
        <Header />
        <Body />
        <Footer />
      </Router>
    </div>
  );
};

export default App;
