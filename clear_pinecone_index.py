#!/usr/bin/env python3
"""
Pinecone Index Cleaner for Peter Lynch Investment Q&A Chatbot

This script clears all vectors from the Pinecone index.
Usage:
    python clear_pinecone_index.py [--confirm]
"""

import asyncio
import argparse
import logging
import os
import sys
from pathlib import Path

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.services.vector_store import VectorStore

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Main function to clear Pinecone index"""
    parser = argparse.ArgumentParser(description='Clear all vectors from Pinecone index')
    parser.add_argument('--confirm', action='store_true', 
                        help='Skip confirmation prompt and proceed with deletion')
    
    args = parser.parse_args()
    
    try:
        # Initialize vector store
        logger.info("🔗 Connecting to Pinecone...")
        vector_store = VectorStore()
        
        # Get index stats before deletion
        logger.info("📊 Checking current index status...")
        stats = await vector_store.get_index_stats()
        
        if stats:
            total_vectors = stats.get('total_vector_count', 0)
            logger.info(f"📈 Current vectors in index: {total_vectors}")
            
            if total_vectors == 0:
                logger.info("✅ Index is already empty!")
                return 0
        else:
            logger.warning("⚠️ Could not retrieve index stats")
        
        # Confirmation prompt
        if not args.confirm:
            logger.warning("🚨 WARNING: This will delete ALL vectors from the Pinecone index!")
            logger.warning("🚨 This action cannot be undone!")
            
            response = input("\nAre you sure you want to proceed? Type 'yes' to confirm: ")
            
            if response.lower() != 'yes':
                logger.info("❌ Operation cancelled by user")
                return 0
        
        # Clear the index
        logger.info("🗑️ Clearing Pinecone index...")
        success = await vector_store.clear_all_vectors()
        
        if success:
            logger.info("✅ Successfully cleared all vectors from Pinecone index!")
            
            # Verify deletion
            logger.info("🔍 Verifying deletion...")
            await asyncio.sleep(2)  # Give Pinecone time to process
            
            new_stats = await vector_store.get_index_stats()
            if new_stats:
                remaining_vectors = new_stats.get('total_vector_count', 0)
                if remaining_vectors == 0:
                    logger.info("✅ Verification successful: Index is now empty")
                else:
                    logger.warning(f"⚠️ Verification: {remaining_vectors} vectors still remain (may take time to update)")
            
            logger.info("🎉 Pinecone index cleared successfully!")
            logger.info("💡 You can now load fresh data using: python load_csv_data.py")
            return 0
        else:
            logger.error("❌ Failed to clear Pinecone index")
            return 1
            
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)