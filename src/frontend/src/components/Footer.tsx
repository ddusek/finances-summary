import React from 'react';
import styled from 'styled-components';
import { COLOR_DARK } from '../utils/cssConstants';

const Container = styled.div`
  background-color: ${COLOR_DARK};
  height: 60px;
`;

const Footer: React.FC = () => {
  return (
    <Container>
      <span>footer</span>
    </Container>
  );
};

export default Footer;
