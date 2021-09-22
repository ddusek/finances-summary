import React from 'react';
import { Switch, Route, withRouter } from 'react-router-dom';
import styled from 'styled-components';
import { COLOR_GREY } from '../utils/cssConstants';
import Home from '../pages/Home';
import SignUp from '../pages/SignUp';
import SignIn from '../pages/SignIn';

const Container = styled.div`
  background-color: ${COLOR_GREY};
`;

const Body: React.FC = () => {
  return (
    <Container>
      <Switch>
        <Route path="/sign-up" component={withRouter(SignUp)} />
        <Route path="/sign-in" component={withRouter(SignIn)} />
        <Route path="/" component={withRouter(Home)} />
      </Switch>
    </Container>
  );
};

export default Body;
