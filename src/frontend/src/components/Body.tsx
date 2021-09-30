import React from 'react';
import { Switch, Route } from 'react-router-dom';
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
        <Route path="/sign-up" component={SignUp} />
        <Route path="/sign-in" component={SignIn} />
        <Route path="/" component={Home} />
      </Switch>
    </Container>
  );
};

export default Body;
