import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { createGlobalStyle } from 'styled-components';
import { COLOR_WHITE } from './constants';
import Header from './components/header/header';
import Body from './components/body';
import Footer from './components/footer';

const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    color: ${COLOR_WHITE};
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
      'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
      sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
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
