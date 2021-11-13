import React from 'react';
import { Switch, Route } from 'react-router-dom';
import styled from 'styled-components';
import { COLOR_DARK_GREY } from '../utils/cssConstants';
import Home from '../pages/Home';
import SignUp from '../pages/SignUp';
import SignIn from '../pages/SignIn';
import MyStocks from '../pages/MyStocks';
import NotFound from '../pages/NotFound';
import TransactionsHistoryPage from '../pages/TransactionsHistoryPage';

const Container = styled.div`
  background-color: ${COLOR_DARK_GREY};
`;

const Body = () => {
  return (
    <Container>
      <Switch>
        <Route path="/sign-up" component={SignUp} />
        <Route path="/sign-in" component={SignIn} />
        <Route path="/my-stocks" component={MyStocks} />
        <Route path="/list-commodities" component={TransactionsHistoryPage} />
        <Route path="/" exact component={Home} />
        <Route component={NotFound} />
      </Switch>
    </Container>
  );
};

export default Body;
