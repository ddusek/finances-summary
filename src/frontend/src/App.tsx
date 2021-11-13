import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { useMediaQuery } from 'react-responsive';
import { createGlobalStyle } from 'styled-components';
import { COLOR_FONT, COLOR_TEAL, COLOR_DARK_GREY } from './utils/cssConstants';
import Header from './components/header/Header';
import Body from './components/Body';
import Footer from './components/Footer';
import { UserContext, initialUser, User } from './context/User';
import { ResponsivityContext, Responsivity } from './context/Responsivity';
import { UserVerify } from './api/requests';

const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    color: ${COLOR_FONT};
    background-color: ${COLOR_DARK_GREY};
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

const App = () => {
  const [user, setUser] = useState<User>(initialUser);
  const responsivity: Responsivity = {
    isMobile: useMediaQuery({ maxWidth: 719 }),
    isTablet: useMediaQuery({ minWidth: 720, maxWidth: 1279 }),
    isDesktop: useMediaQuery({ minWidth: 1280 }),
  };
  useEffect(() => {
    UserVerify()
      .then((res) => {
        if (res.data.authorized) {
          setUser({ loggedIn: true, username: 'todo' });
          console.log('token');
        } else {
          setUser({ loggedIn: false, username: '' });
          console.log('no token');
        }
      })
      .catch(() => {
        setUser({ loggedIn: false, username: '' });
        console.log('err no token');
      });
  }, []);
  return (
    <div className="App">
      <GlobalStyle />
      <ResponsivityContext.Provider value={responsivity}>
        <UserContext.Provider value={user}>
          <Router>
            <Header />
            <Body />
            <Footer />
          </Router>
        </UserContext.Provider>
      </ResponsivityContext.Provider>
    </div>
  );
};

export default App;
