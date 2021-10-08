import React from 'react';
import styled from 'styled-components';
import { COLOR_GREY } from '../utils/cssConstants';

const Container = styled.div`
  background-color: ${COLOR_GREY};
`;

const NotFound: React.FC = () => {
  return (
    <Container>
      <span>Not found</span>
    </Container>
  );
};

export default NotFound;
