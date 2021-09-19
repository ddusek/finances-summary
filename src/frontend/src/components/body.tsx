import React from 'react';
import { Switch, Route, withRouter } from 'react-router-dom';
import styled from 'styled-components';
import { COLOR_GREY } from '../constants';
import Home from './home';

const Container = styled.div`
  background-color: ${COLOR_GREY};
  height: 100%;
`;

const Body: React.FC = () => {
  return (
    <Container>
      <Switch>
        <Route path="/a" component={withRouter(Home)} />
      </Switch>
    </Container>
  );
};

export default Body;
