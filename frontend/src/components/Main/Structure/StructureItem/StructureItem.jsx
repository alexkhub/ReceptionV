import structureItemUser from "../../../../images/structure-item-user-img.png";

function StructureItem(props) {
  return (
    <div className="structure-item">
      <img src={structureItemUser} alt="user img" />
      <div>
        <p>{props.name}</p>
        <p>{props.description}</p>
      </div>
    </div>
  );
}

export default StructureItem;
