"""Command-line entry point for the capstone training application."""

import argparse
from pathlib import Path

import torch

from mini_project.config import TrainingConfig
from mini_project.data import create_loaders
from mini_project.engine import evaluate, train_one_epoch
from mini_project.model import Classifier


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train the capstone classifier")
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--output", type=Path, default=Path("artifacts/model.pt"))
    return parser.parse_args()


def run(config: TrainingConfig, output: Path) -> float:
    config.validate()
    torch.manual_seed(config.seed)
    training_loader, validation_loader = create_loaders(config)
    model = Classifier(config.hidden_features).to(config.device)
    optimizer = torch.optim.SGD(model.parameters(), lr=config.learning_rate)

    for epoch in range(config.epochs):
        loss = train_one_epoch(model, training_loader, optimizer, config.device)
        accuracy = evaluate(model, validation_loader, config.device)
        print(f"epoch={epoch + 1:02d}, loss={loss:.4f}, val_accuracy={accuracy:.3f}")

    output.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), output)
    print(f"checkpoint={output}")
    return accuracy


def main() -> None:
    args = parse_args()
    config = TrainingConfig(epochs=args.epochs)
    run(config, args.output)


if __name__ == "__main__":
    main()
