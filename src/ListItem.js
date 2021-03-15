import { React } from "react";
import PropTypes from 'prop-types';

export function ListItem(props) {
  return <p>{props.name}</p>;
}

ListItem.propTypes = {
  name: PropTypes.node.isRequired,
}