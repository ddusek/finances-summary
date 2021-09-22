import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import { COLOR_TEAL } from '../../utils/cssConstants';

const Container = styled.ul`
  margin-right: 15px;
  font-size: 22px;
`;

const Normal = styled.li`
  border: 2px transparent solid;
  display: block;
  position: relative;
  padding: 0.2em 0;
  :after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 0.1em;
    background-color: ${COLOR_TEAL};
    opacity: 0;
    transition: opacity 300ms, transform 300ms;
  }
  ::after {
    opacity: 1;
    transform: scale(0);
    transform-origin: center;
  }
  :hover::after,
  :focus::after {
    transform: scale(1);
  }
`;

const Highlight = styled(Normal)`
  font-weight: 500;
`;

export interface NavigationItemProps {
  link: string;
  text: string;
  highlight?: boolean;
}

const HighlightItem: React.FC<NavigationItemProps> = (
  props: NavigationItemProps
) => {
  return (
    <Highlight>
      <Link to={props.link}>{props.text}</Link>
    </Highlight>
  );
};

const NormalItem: React.FC<NavigationItemProps> = (
  props: NavigationItemProps
) => {
  return (
    <Normal>
      <Link to={props.link}>{props.text}</Link>
    </Normal>
  );
};

const NavigationItem: React.FC<NavigationItemProps> = (
  props: NavigationItemProps
) => {
  return (
    <Container>
      {props.highlight ? HighlightItem(props) : NormalItem(props)}
    </Container>
  );
};

export default NavigationItem;
