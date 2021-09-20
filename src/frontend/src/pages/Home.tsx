import React from 'react';
import styled from 'styled-components';
import { COLOR_GREY } from '../constants';

const Container = styled.div`
  background-color: ${COLOR_GREY};
`;

const Home: React.FC = () => {
  return (
    <Container>
      <span>home</span>
    </Container>
  );
};

export default Home;
