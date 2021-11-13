import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAlignJustify } from '@fortawesome/free-solid-svg-icons';
import { HamburgerMenu } from './HamburgerMenu';
import { MenuItem } from '../../interfaces';

export const Hamburger = (props: { items: MenuItem[] }) => {
  return (
    <div>
      <span>
        <FontAwesomeIcon icon={faAlignJustify} />
      </span>
      <HamburgerMenu items={props.items} />
    </div>
  );
};
